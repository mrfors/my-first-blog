

<table id="calendar1">
  <thead>
    <tr><td colspan="4"><td colspan="3">
    <tr><td>Пн<td>Вт<td>Ср<td>Чт<td>Пт<td>Сб<td>Вс
  <tbody>
</table>

<script>
var D1 = new Date(),
    D1last = new Date(D1.getFullYear(),D1.getMonth()+1,0).getDate(), // последний день месяца
    D1Nlast = new Date(D1.getFullYear(),D1.getMonth(),D1last).getDay(), // день недели последнего дня месяца
    D1Nfirst = new Date(D1.getFullYear(),D1.getMonth(),1).getDay(), // день недели первого дня месяца
    calendar1 = '<tr>',
    month=["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]; // название месяца, вместо цифр 0-11

// пустые клетки до первого дня текущего месяца
if (D1Nfirst != 0) {
  for(var  i = 1; i < D1Nfirst; i++) calendar1 += '<td>';
}else{ // если первый день месяца выпадает на воскресенье, то требуется 7 пустых клеток
  for(var  i = 0; i < 6; i++) calendar1 += '<td>';
}

// дни месяца
for(var  i = 1; i <= D1last; i++) {
  if (i != D1.getDate()) {
    calendar1 += '<td>' + i;
  }else{
    calendar1 += '<td id="today">' + i;  // сегодняшней дате можно задать стиль CSS
  }
  if (new Date(D1.getFullYear(),D1.getMonth(),i).getDay() == 0) {  // если день выпадает на воскресенье, то перевод строки
    calendar1 += '<tr>';
  }
}

// пустые клетки после последнего дня месяца
if (D1Nlast != 0) {
  for(var  i = D1Nlast; i < 7; i++) calendar1 += '<td>';
}

document.querySelector('#calendar1 tbody').innerHTML = calendar1;
document.querySelector('#calendar1 thead td:last-child').innerHTML = D1.getFullYear();
document.querySelector('#calendar1 thead td:first-child').innerHTML = month[D1.getMonth()];
</script>

Выпадающий календарь в input

Типы input описаны здесь. Среди них есть несколько для дат
вид 	код 	формат 	описание
	<input type="date" value="2012-04-10"/> 	yyyy-mm-dd 	дата
	<input type="datetime" value="2012-04-10T20:37:40"/> 	yyyy-mm-ddTHH:MM:SS 	дата и время с часовым поясом, нет поддержки, работает как type="text"
	<input type="datetime-local" value="2012-04-10T20:37:40"/> 	yyyy-mm-ddTHH:MM:SS 	дата и время
	<input type="month" value="2012-04"/> 	yyyy-mm 	год и месяц
	<input type="week" value="2012-W46"/> 	yyyy-W 	год и порядковый номер недели
	<input type="time" value="20-37"/> 	HH:MM:SS (секунды не обязательны) 	вр
