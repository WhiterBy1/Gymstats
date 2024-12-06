export class WorkoutTracker {
    constructor() {
        this.currentWorkout = null;
    }

    startWorkout() {
        this.currentWorkout = {
            date: new Date(),
            exercises: [],
            startTime: new Date()
        };
    }

    addExerciseSet(exerciseId, weight, reps, rpe, restTime) {
        if (!this.currentWorkout) return;

        const set = {
            weight,
            reps,
            rpe,
            restTime,
            timestamp: new Date()
        };

        let exercise = this.currentWorkout.exercises.find(e => e.id === exerciseId);
        if (!exercise) {
            exercise = {
                id: exerciseId,
                sets: []
            };
            this.currentWorkout.exercises.push(exercise);
        }

        exercise.sets.push(set);
    }

    finishWorkout() {
        if (!this.currentWorkout) return;

        this.currentWorkout.endTime = new Date();
        // Here we would typically save the workout data
        // This will be integrated with the backend later
        
        const workout = this.currentWorkout;
        this.currentWorkout = null;
        return workout;
    }
}