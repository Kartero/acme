import { createApp } from 'vue';
import Exercise from './components/exercise/root.vue';

const url = new URL(window.location.href);
const pathName = url.pathname;

switch (pathName) {
    case '/exercise/':
        createApp(Exercise).mount('#vue-app');
        break;
}


/*
createApp({
    data() {
        return {
            title: '<h2>Toimii!</h2>'
        }
    },
    compilerOptions: {
        delimiters: ['[[', ']]']
    }
}).mount('#vue-app');
*/