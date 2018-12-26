$.fn.dateTime = function(){
	var arMonth = new Array("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")
		,clock = function($e){
			var d = new Date()
				,month = arMonth[d.getMonth()]
				,day = d.getDate()
				,hours = d.getHours()
				,minutes = d.getMinutes();
			if(day <= 9) day = "0" + day;
			if(hours <= 9) hours = "0" + hours;
			if(minutes <= 9) minutes = "0" + minutes;
			$e.html(day + " " + month + " " + d.getFullYear() + ",&nbsp;"+ hours + ":" + minutes);
		};
	return this.each(function(){
		var $e = $(this);
		clock($e);
		window.setInterval(function(){
			clock($e);
		},60000);
	});
};


$(function(){
	$('.logo_panel .data').dateTime();


	//высота центрального блока
	//.content .center_block
	function content_height(){
		var content_height = $('.content').height();
		var center_block_height = $('.content .center_block').height();
		if(content_height > center_block_height){
			$('.content .center_block').height(content_height);
		};
	};
	content_height();
	$(window).resize(content_height);
});