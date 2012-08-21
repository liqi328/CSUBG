
window.onload = window.onresize = window.onscroll = function ()
{
	var oBox = document.getElementById("divQQbox");	
	var oLine = document.getElementById("divOnline");
	var oMenu = document.getElementById("divMenu");
	var iScrollTop = document.documentElement.scrollTop || document.body.scrollTop;
	setTimeout(function ()
	{
		clearInterval(oBox.timer);
		var iTop = parseInt((document.documentElement.clientHeight - oBox.offsetHeight)/2) + iScrollTop;
		oBox.timer = setInterval(function ()
		{
			var iSpeed = (iTop - oBox.offsetTop) / 8;
			iSpeed = iSpeed > 0 ? Math.ceil(iSpeed) : Math.floor(iSpeed);
			oBox.offsetTop == iTop ? clearInterval(oBox.timer) : (oBox.style.top = oBox.offsetTop + iSpeed + "px");
		}, 30)
	}, 100)
	
	oBox.onmouseover = function ()
	{
		this.style.width = 131 + "px";
		oLine.style.display = "block";
		oMenu.style.display = "none";
	};
	oBox.onmouseout = function ()
	{
		this.style.width = '';
		oLine.style.display = "none";
		oMenu.style.display = "block";
	};
};