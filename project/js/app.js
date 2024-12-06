import { WorkoutPlanner } from './workoutPlanner.js';
import { WorkoutTracker } from './workoutTracker.js';
import { Statistics } from './statistics.js';
import { UIManager } from './uiManager.js';

class App {
    constructor() {
        this.planner = new WorkoutPlanner();
        this.tracker = new WorkoutTracker();
        this.stats = new Statistics();
        this.ui = new UIManager();
        
        this.initializeApp();
    }

    initializeApp() {
        // Initialize navigation
        document.querySelectorAll('.nav-links li').forEach(link => {
            link.addEventListener('click', (e) => {
                this.ui.switchView(e.currentTarget.dataset.view);
            });
        });

        // Initialize the planner view
        this.planner.initialize();
    }
}

// Start the application
window.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});