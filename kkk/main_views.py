from django.http import HttpResponse
from django.template import Context, loader
from kkk.models import *
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
def main_page(req):
    c = {}
    c.update(csrf(req))
    return render_to_response('login.html',c)

def login(req):
    uid = req.POST['user_id']
    pw = req.POST['user_pw']
    registed = User.objects.filter(user_id=uid).count()
    if registed > 0:
        user_data = User.objects.get(user_id=uid)
        if user_data.user_pw == pw:
            req.session['name'] = user_data.user_name
            return HttpResponseRedirect('/board')
        else:
            return HttpResponse("pw")
    else:
        return HttpResponse("id")

def board_page(req):
    boardList = Board.objects.order_by('-id')
    totalCnt = Board.objects.all().count()
    print 'totalCnt', totalCnt
    tpl = loader.get_template('board_list.html')
    ctx = Context({'boardList' : boardList, 'totalCnt' : totalCnt})
    html = tpl.render(ctx)
    return HttpResponse(html)
 
def write_page(req):
    c = {}
    c.update(csrf(req))
    return render_to_response('write_page.html',c)

def write_board(req):
    print 'totalCnt', 'aaaa'
    br = Board (user_id = req.session['name'],
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
    br = User  (user_id = req.POST['user_id'],
                user_pw = req.POST['user_pw'],
                user_name = req.POST['user_name']
                )
    br.save()
    
    url = 'http://127.0.0.1:8000' 
    return HttpResponseRedirect(url)

def view_page(req):
    vid = req.GET['view_id']
    board_data = Board.objects.get(id=vid)
    Board.objects.filter(id=vid).update(count = board_data.count + 1)
    return render_to_response('view_page.html', {'board_data': board_data })  
    
