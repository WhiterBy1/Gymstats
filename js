        let currentWeekOffset = 0;
        const weekData = {};
        let activeModal = null;

        const diasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];

    
        function formatDate(date, includeYear = false) {
            const options = {
                month: 'short', 
                day: 'numeric', 
                ...(includeYear && { year: 'numeric' }), 
                timeZone: 'America/Bogota' 
            };
            return new Intl.DateTimeFormat('es-CO', options).format(date);
        }

        function getCurrentWeek(offset = 0) {
            const now = new Date();
            now.setDate(now.getDate() + offset * 7);
            const startOfWeek = new Date(now);
            startOfWeek.setDate(now.getDate() - ((now.getDay() + 6) % 7)); 
            const endOfWeek = new Date(startOfWeek);
            endOfWeek.setDate(startOfWeek.getDate() + 6);
            return { start: startOfWeek, end: endOfWeek };
        }

        function renderCalendar() {
            const week = getCurrentWeek(currentWeekOffset);
            const days = [];
            for (let i = 0; i < 7; i++) {
                const day = new Date(week.start);
                day.setDate(day.getDate() + i);
                days.push(day);
            }

            const weekKey = `${week.start.toDateString()} - ${week.end.toDateString()}`;
            if (!weekData[weekKey]) {
                weekData[weekKey] = Array(7).fill('');
            }

            return `
                <div class="calendar">
                    <button onclick="navigateWeek(-1)">⟵</button>
                    <h3>${formatDate(week.start, true)} - ${formatDate(week.end, true)}</h3> 
                    <button onclick="navigateWeek(1)">⟶</button>
                </div>
                <div class="day-boxes">
                    ${diasSemana.map((dia, index) => {
                        const formattedDate = formatDate(days[index]); 

                        return `
                            <div class="day-box">
                                <h4>${dia}</h4>
                                <span class="date">${formattedDate}</span>
                                <button onclick="openModal('${weekKey}', ${index})">+ Agregar ejercicio </button>
                                <div class="modal" id="modal-${weekKey}-${index}">
                                    <textarea oninput="resizeTextArea(this)">${weekData[weekKey][index]}</textarea>
                                    <button onclick="saveData('${weekKey}', ${index})">Guardar</button>
                                    <button onclick="closeModal()">Cerrar</button>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            `;
        }

        function resizeTextArea(textarea) {
            textarea.style.height = 'auto';
            textarea.style.height = (textarea.scrollHeight) + 'px';
        }

        function navigateWeek(offset) {
            closeModal();
            currentWeekOffset += offset;
            changeContent('planeacion');
        }

        function openModal(weekKey, dayIndex) {
            closeModal();
            const modal = document.getElementById(`modal-${weekKey}-${dayIndex}`);
            modal.style.display = 'block';
            activeModal = modal;
        }

        function closeModal() {
            if (activeModal) {
                activeModal.style.display = 'none';
                activeModal = null;
            }
        }

        function saveData(weekKey, dayIndex) {
            const modal = document.getElementById(`modal-${weekKey}-${dayIndex}`);
            const textarea = modal.querySelector('textarea');
            weekData[weekKey][dayIndex] = textarea.value;
            closeModal();
        }

        function changeContent(option, element) {
            const mainContent = document.getElementById('main-content');
            const allNavItems = document.querySelectorAll('.nav');
            allNavItems.forEach(item => item.parentElement.classList.remove('selected'));
            if (element) element.parentElement.classList.add('selected');

            let content = '';

            if (option === 'planeacion') {
                content = renderCalendar();
            } else if (option === 'entrenamiento') {
                content = `
                    <h2>Entrenamiento Actual</h2>
                    <p>Revisa y sigue tu rutina de ejercicios actual.</p>
                `;
            } else if (option === 'estadisticas') {
                content = `
                    <h2>Estadísticas</h2>
                    <p>Consulta tu progreso y logros alcanzados.</p>
                `;
            }

            mainContent.innerHTML = content;
        }
