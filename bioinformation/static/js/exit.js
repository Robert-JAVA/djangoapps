$(function(){
	$(".exit").click(function(){
		if(confirm("确认注销吗?")){
			return true;
		}
		return false;
	});
	$("input[type='submit']").click(function(){
		if($("input[name='resourcetype']").val()==""){
			alert("请选择资源类型!");
			return false;
		}
		if($("input[name='filetype']").val()==""){
			alert("请选择文件类型!");
			return false;
		}
		if($("input[name='filename']").val()==""){
			alert("请选择所要上传的文件!");
			return false;
		}
		return true;
	});
});