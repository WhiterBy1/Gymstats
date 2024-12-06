export class UIManager {
    constructor() {
        this.currentView = 'planner';
    }

    switchView(viewName) {
        // Hide all views
        document.querySelectorAll('.view').forEach(view => {
            view.classList.remove('active');
        });

        // Show selected view
        document.getElementById(`${viewName}-view`).classList.add('active');

        // Update navigation
        document.querySelectorAll('.nav-links li').forEach(link => {
            link.classList.remove('active');
            if (link.dataset.view === viewName) {
                link.classList.add('active');
            }
        });

        this.currentView = viewName;
    }

    showNotification(message, type = 'info') {
        // Implementation for showing notifications will be added later
    }

    showConfirmDialog(message) {
        return confirm(message); // This will be replaced with a custom dialog later
    }
}