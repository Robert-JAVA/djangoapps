$(function(){
	$(".exit").click(function(){
		if(confirm("ȷ��ע����?")){
			return true;
		}
		return false;
	});
	$("input[type='submit']").click(function(){
		if($("input[name='resourcetype']").val()==""){
			alert("��ѡ����Դ����!");
			return false;
		}
		if($("input[name='filetype']").val()==""){
			alert("��ѡ���ļ�����!");
			return false;
		}
		if($("input[name='filename']").val()==""){
			alert("��ѡ����Ҫ�ϴ����ļ�!");
			return false;
		}
		return true;
	});
});