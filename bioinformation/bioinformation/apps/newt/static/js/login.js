$(function(){
	$("input[type='submit']").click(function(){
		if($("input[name='name']").val()== ""){
			alert("ÇëÌîĞ´ÓÃ»§Ãû³Æ!");
			return false;
		}
		if($("input[name='password']").val()==""){
			alert("ÇëÊäÈëÃÜÂë!");
			return false;
		}
		return true;
	});
});