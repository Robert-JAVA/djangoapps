$(function(){
	$("input[type='submit']").click(function(){
		if($("input[name='name']").val()==""){
			alert("����д�û�����!");
			return false;
		}
		if($("input[name='email']").val()==""){
			alert("�����������ַ!");
			return false;
		}
		if($("input[name='password1']").val()==""){
			alert("����������!");
			return false;
		}
		if($("input[name='password']").val()==""){
			alert("��ȷ������!");
			return false;
		}
		if($("input[name='password1']").val()!=$("input[name='password']").val()){
			alert("�����������벻һ��,����������!");
			$("input[name='password']").val("");
			$("input[name='password']").focus();
			return false;
		}
		return true;
	});
});
