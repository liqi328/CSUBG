var g_aData=
[
	'点击可查看软件详细说明，and 提供下载 ^_^!',
];

var g_oTimerHide=null;

window.onload=function ()
{
	var aLi=document.getElementById('content').getElementsByTagName('li');
	
	bindTopic(aLi);
};

function bindTopic(aElement)
{
	var i=0;
	
	for(i=0;i<aElement.length;i++)
	{
		aElement[i].miaovIndex=i;
		aElement[i].onmouseover=function (ev){showTopic(this.miaovIndex, window.event || ev);};
		aElement[i].onmouseout=function (){hideTopic();};
		aElement[i].onmousemove=function (ev)
		{
			var oEvent=window.event || ev;
			setPosition(oEvent.clientX, oEvent.clientY);
		};
	}
}

function showTopic(index, oEvent)
{
	var oTopic=document.getElementById('topic');
	
	if(g_oTimerHide)
	{
		clearTimeout(g_oTimerHide);
	}
	
	oTopic.getElementsByTagName('div')[1].innerHTML=g_aData[0];
	oTopic.style.display='block';
	
	setPosition(oEvent.clientX, oEvent.clientY);
}

function hideTopic()
{
	var oTopic=document.getElementById('topic');
	
	if(g_oTimerHide)
	{
		clearTimeout(g_oTimerHide);
	}
	g_oTimerHide=setTimeout
	(
		function ()
		{
			oTopic.style.display='none';
		},50
	);
}

function setPosition(x, y)
{
	var top=document.body.scrollTop || document.documentElement.scrollTop;
	var left=document.body.scrollLeft || document.documentElement.scrollLeft;
	
	x+=left;
	y+=top;
	
	var oTopic=document.getElementById('topic');
	var l=x+20;
	var t=y-(oTopic.offsetHeight-20);
	var bRight=true;
	var iPageRight=left+document.documentElement.clientWidth;
	
	if(l+oTopic.offsetWidth>iPageRight)
	{
		bRight=false;
		
		l=x-(oTopic.offsetWidth+20);
		oTopic.getElementsByTagName('div')[0].className='adorn_r';
	}
	else
	{
		oTopic.getElementsByTagName('div')[0].className='adorn';
	}
	
	oTopic.style.left=l+'px';
	oTopic.style.top=t+'px';
}
