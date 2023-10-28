new Vue({
  el: '#app',
  data: { 
    attrs: [
        {
          key: 'today',
          highlight: {
            backgroundColor: '#ff8080',
          },
          dates: new Date(),
          popover: {
            label: 'メッセージを表示できます',
          },
        }
    ],
  }
})