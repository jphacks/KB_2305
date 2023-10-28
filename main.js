import users from './assets/data.json'

export default {
  data: () => {
     users: users
  }
}


new Vue({
    el: '#to-do',
    data: {
      newTask: '',
      todos: [
        { task: 'Rubyの勉強をする', isCompleted: false },
        { task: 'Vue.jsのアプリを作る', isCompleted: false },
        { task: 'Youtubeをみる', isCompleted: false }
      ]
    },
    methods: {
      addTodo: function() {
        if (this.newTask == '') return;
        this.todos.push(
          { task: this.newTask, isCompleted: false }
        );
        this.newTask = '';
      },
      deleteTodo: function (todo) {
        var index = this.todos.indexOf(todo)
        this.todos.splice(index, 1)
      }
    }
  });