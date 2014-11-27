from django.http import HttpResponse,HttpResponseRedirect
from kkk.models import Board
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def main_page(req):
    if req.user.is_authenticated():
        return HttpResponseRedirect('/board')
    else:
        return HttpResponseRedirect('/login_page')

def login_page(req):
    c = {}
    c.update(csrf(req))
    return render_to_response('login.html',c)

def login_proc(req):
    uid = req.POST['user_id']
    pw = req.POST['user_pw']
    user = authenticate(username=uid, password=pw)
    if user is not None:
        if user.is_active:
            login(req, user)
            return HttpResponseRedirect('/board')
        else:
            print 'cause', 'not active'
            return HttpResponseRedirect('/login_page')
    else:
        print 'cause', 'no info'
        return HttpResponseRedirect('/login_page')

def logout_proc(req):
    logout(req)
    return HttpResponseRedirect('/login_page')

def board_page(req):
    if not req.user.is_authenticated():
        print 'auth', req.user.is_authenticated()
        return HttpResponseRedirect('/login_page')
    boardList = Board.objects.order_by('-id')
    totalCnt = Board.objects.all().count()
    return render_to_response('board_list.html', {'boardList' : boardList, 'totalCnt' : totalCnt})

 
def write_page(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login_page')
    c = {}
    c.update(csrf(req))
    return render_to_response('write_page.html',c)

def write_board(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login_page')
    br = Board (user_id = req.user.email,
                board_title = req.POST['board_title'],
                board_content = req.POST['board_content'],
                count = 0
                )
    br.save()
    return HttpResponseRedirect('/board')    
    
def regist_page(req):
    c = {}
    c.update(csrf(req))
    return render_to_response('regist_page.html',c)

def regist_user(req):
    user = User.objects.create_user(req.POST['user_id'], req.POST['user_name'], req.POST['user_pw'])
    user.is_staff = False
    user.save()
    return HttpResponseRedirect('/login_page')

def view_page(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login_page')
    vid = req.GET['view_id']
    board_data = Board.objects.get(id=vid)
    Board.objects.filter(id=vid).update(count = board_data.count + 1)
    board_data = Board.objects.get(id=vid)
    return render_to_response('view_page.html', {'board_data' : board_data, 'user_data' : req.user})

def modify_page(req):
    if not req.user.is_authenticated():
        return HttpResponseRedirect('/login_page')
    vid = req.GET['view_id']
    board_data = Board.objects.get(id=vid)
    c = {'board_data' : board_data}
    c.update(csrf(req))
    return render_to_response('modify_page.html',c)

def modify(req):
    vid = req.POST['view_id']
    board_data = Board.objects.get(id=vid)
    Board.objects.filter(id=vid).update(board_title = req.POST['board_title'],board_content = req.POST['board_content'])
    return HttpResponseRedirect('/board')

def delete(req):
    vid = req.GET['view_id']
    board_data = Board.objects.get(id=vid)
    board_data.delete()
    return HttpResponseRedirect('/board')

