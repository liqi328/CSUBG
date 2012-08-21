 
var RollText = function(cName,color1,color2){this.initialize(cName,color1,color2);}
RollText.prototype = {
	initialize:function(cName,color1,color2){
		var self = this;
		var obj = self.getClass(document.body,cName);
		for(var i=0;i<obj[0].getElementsByTagName("li").length;i++){
			var li = obj[0].getElementsByTagName("li")[i];
			li.style.position = "relative";
			li.style.overflow = "hidden";
			var text = li.getElementsByTagName("a")[0];
			text.style.position = "absolute";
			text.style.textDecoration = "none";
			text.innerHTML = "<font color="+color1+">" + text.innerHTML + "</font><br /><font color="+color2+">" + text.innerHTML + "</font>";
			text.onmouseover = function(){
				self.startMove(this,{"marginTop":-li.offsetHeight});
			}
			text.onmouseout = function(){
				self.startMove(this,{"marginTop":0});
			}
		}
	},
	getClass	:	function(oParent, sClass){
		var aElem = oParent.getElementsByTagName('*');
		var aClass = [];
		var i = 0;
		for(i=0;i<aElem.length;i++)if(aElem[i].className == sClass)aClass.push(aElem[i]);
		return aClass;
	},
	startMove	:	function(target, object, onComplete){
		var self = this;
		if(target.timer)clearInterval(target.timer);
		target.timer = setInterval(function (){
			self.doMove(target, object, onComplete);
		}, 30);
	},
	doMove	:	function(target, object, onComplete){
		var iCur = 0;
		var attr = '';
		var bStop = true;
		var self = this;
		for(attr in object){
			attr == 'opacity' ? iCur = parseInt(parseFloat(self.getStyle(target, 'opacity'))*100) : iCur = parseInt(self.getStyle(target, attr));
			if(isNaN(iCur))iCur = 0;
			if(navigator.userAgent.indexOf("Firefox") > 0){
				var iSpeed = (object[attr]-iCur) / 3;
			}else{
				var iSpeed = (object[attr]-iCur) / 3;
			}
			iSpeed = iSpeed > 0 ? Math.ceil(iSpeed) : Math.floor(iSpeed);
			if(parseInt(object[attr])!=iCur)bStop = false;
			if(attr=='opacity'){
				target.style.filter = "alpha(opacity:"+(iCur+iSpeed)+")";
				target.style.opacity = (iCur + iSpeed) / 100;
			}else{
				attr == 'zIndex' ? target.style[attr] = iCur + iSpeed : target.style[attr] = iCur + iSpeed +'px';
			}
		}
		if(bStop){
			clearInterval(target.timer);
			target.timer = null;		
			if(onComplete)onComplete();
		}
	},
	getStyle	:	function(target, attr){
		return target.currentStyle?target.currentStyle[attr]:getComputedStyle(target, false)[attr];
	}
}
 
/**
* �÷�����
* @method	RollText(cName,color1,color2);
* @param	cName Ҫ���õ���class
* @param	color1 Ĭ��ʱ������ɫ
* @param	color1 ��꾭��������ʾ��������ɫ
* ע����ɫֵҪдȫ����#000000������IE�Ǽ�������ʾ�����õ���ɫ
*/
window.onload = function(){
	//�����б�չʾ
	//��վ�˵�չʾ
	var rollMenu = new RollText("box","#000000","#CC6000");	
}
 