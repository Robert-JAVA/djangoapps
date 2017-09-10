$(function(){
	$("input[type='submit']").click(function(){
		if($("input[name='name']").val()==""){
			alert("请填写用户名称!");
			return false;
		}
		if($("input[name='email']").val()==""){
			alert("请输入邮箱地址!");
			return false;
		}
		if($("input[name='password1']").val()==""){
			alert("请输入密码!");
			return false;
		}
		if($("input[name='password']").val()==""){
			alert("请确认密码!");
			return false;
		}
		if($("input[name='password1']").val()!=$("input[name='password']").val()){
			alert("两次密码输入不一致,请重新输入!");
			$("input[name='password']").val("");
			$("input[name='password']").focus();
			return false;
		}
		return true;
	});
});
