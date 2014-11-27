function loginsubmit(){
var loginform;
loginform = document.getElementById('loginform');
    if (!loginform.user_id.value) {
            alert("ID를 입력하세요");
            loginform.user_id.focus();
            return false;
        }
        if (!loginform.user_pw.value) {
            alert("Password를 입력하세요");
            loginform.user_pw.focus();
            return false;
    }        
                
    loginform.submit();   
}
function registsubmit(){
    var form = document.getElementById('registform');
        if (!form.user_id.value) 
        {
            alert("ID를 적어주세요"); 
            form.user_id.focus(); 
            return false;
        }
        if (!form.user_name.value) {
            alert("닉네임을 적어주세요");
            form.user_name.focus();
            return false;
        }
        if (!form.user_pw.value) {
            alert("비밀번호를 적어주세요");
            form.memo.focus();
            return false;
        } 
		if (form.user_pw.value != form.pw_confirm.value) {
            alert("비밀번호가 일치하지 않습니다.");
            form.memo.focus();
            return false;
        }  
                
        form.submit(); 
}
function writesubmit(){
	var form = document.getElementById('writeform');
        if (!form.board_title.value) {
            alert("제목을 적어주세요");
            form.subject.focus();
            return;
        }
        if (!form.board_content.value) {
            alert("내용을 적어주세요");
            form.memo.focus();
            return;
        }        
                
        form.submit();    
}