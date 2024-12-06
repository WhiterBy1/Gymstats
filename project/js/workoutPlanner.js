export class WorkoutPlanner {
    constructor() {
        this.weekData = {};
        this.currentWeek = new Date();
    }

    initialize() {
        this.setupWeekNavigation();
        this.renderWeek();
    }

    setupWeekNavigation() {
        document.getElementById('prevWeek').addEventListener('click', () => {
            this.currentWeek.setDate(this.currentWeek.getDate() - 7);
            this.renderWeek();
        });

        document.getElementById('nextWeek').addEventListener('click', () => {
            this.currentWeek.setDate(this.currentWeek.getDate() + 7);
            this.renderWeek();
        });
    }

    renderWeek() {
        const weekStart = this.getWeekStart(this.currentWeek);
        document.getElementById('currentWeek').textContent = 
            `Week of ${weekStart.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}`;

        const daysContainer = document.querySelector('.days-container');
        daysContainer.innerHTML = '';

        for (let i = 0; i < 7; i++) {
            const date = new Date(weekStart);
            date.setDate(date.getDate() + i);
            const dayCard = this.createDayCard(date);
            daysContainer.appendChild(dayCard);
        }
    }

    createDayCard(date) {
        const dayCard = document.createElement('div');
        dayCard.className = 'day-card';
        
        const dayName = date.toLocaleDateString('en-US', { weekday: 'long' });
        const dateStr = date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' });

        dayCard.innerHTML = `
            <div class="day-header">
                <span class="day-name">${dayName}</span>
                <span class="date">${dateStr}</span>
            </div>
            <div class="exercises">
                <button class="add-exercise-btn" data-date="${date.toISOString()}">
                    <i class="fas fa-plus"></i> Add Exercise
                </button>
            </div>
        `;

        dayCard.querySelector('.add-exercise-btn').addEventListener('click', () => {
            this.showExerciseModal(date);
        });

        return dayCard;
    }

    showExerciseModal(date) {
        const modal = document.getElementById('exerciseModal');
        modal.style.display = 'block';

        const form = document.getElementById('exerciseForm');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.saveExercise(date, form);
            modal.style.display = 'none';
        });

        document.getElementById('cancelExercise').addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    saveExercise(date, form) {
        const exercise = {
            name: form.exerciseName.value,
            sets: parseInt(form.sets.value),
            planned: []
        };

        // Initialize the week data if it doesn't exist
        const dateStr = date.toISOString().split('T')[0];
        if (!this.weekData[dateStr]) {
            this.weekData[dateStr] = [];
        }

        this.weekData[dateStr].push(exercise);
        this.renderWeek();
        form.reset();
    }

    getWeekStart(date) {
        const result = new Date(date);
        result.setDate(result.getDate() - result.getDay());
        return result;
    }
}