import { Calendar } from '@fullcalendar/core';
import interactionPlugin from '@fullcalendar/interaction';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

function getVacations(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => resolve(xhr.responseText);
    xhr.onerror = () => reject(xhr.statusText);
    xhr.send();
  });
}

const link = 'http://localhost:5000/calendar'

getVacations(link)
  .then(response => {
    console.log(JSON.parse(response))
    //document.addEventListener('DOMContentLoaded', function() {
    let calendarEl = document.getElementById('calendar');
    let calendar = new Calendar(calendarEl, {
      plugins: [ interactionPlugin, dayGridPlugin, timeGridPlugin, listPlugin ],
      header: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
      },
      defaultDate: '2018-01-12',
      navLinks: true, // can click day/week names to navigate views
      editable: true,
      eventLimit: true, // allow "more" link when too many events
      events: JSON.parse(response)
    });
    calendar.render();
    //});
})




