$(function(){
	$("input[type='submit']").click(function(){
		if($("input[name='name']").val()== ""){
			alert("����д�û�����!");
			return false;
		}
		if($("input[name='password']").val()==""){
			alert("����������!");
			return false;
		}
		return true;
	});
});