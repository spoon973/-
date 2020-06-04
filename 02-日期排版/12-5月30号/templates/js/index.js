window.onload = function() {
	var oInput = document.getElementById('btn');
	oInput.onclick = function() {
		alert('这是一个外部引用js文件');
	}
}