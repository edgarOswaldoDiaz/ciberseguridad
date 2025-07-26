# Vue.js 

## Vue CLI Commands
- Create new project: `vue create project-name`
- Start development server: `npm run serve`
- Build for production: `npm run build`
- Lint project: `npm run lint`
- Install Vue CLI globally: `npm install -g @vue/cli`

## Project Structure
- `src/App.vue`: Main app component
- `src/main.js`: Entry point
- `src/components/`: Reusable components
- `src/assets/`: Static assets
- `public/`: Static files served as-is

## Component Syntax
### Basic Component
```vue
<template>
  <div>{{ message }}</div>
</template>

<script>
export default {
  name: 'ComponentName',
  data() {
    return {
      message: 'Hello Vue!'
    }
  }
}
</script>

<style scoped>
div {
  /* Component-specific styles */
}
</style>
```

## Directives
- `v-bind`: Bind attribute `:attribute="value"`
- `v-if`: Conditional rendering `v-if="condition"`
- `v-else`: Else condition for v-if
- `v-else-if`: Else if condition
- `v-show`: Toggle visibility `v-show="condition"`
- `v-for`: List rendering `v-for="item in items"`
- `v-on`: Event handling `@event="handler"`
- `v-model`: Two-way binding `v-model="value"`
- `v-once`: Render once
- `v-html`: Render HTML `v-html="rawHtml"`
- `v-text`: Update text `v-text="text"`
- `v-cloak`: Hide uncompiled template

## Component Properties
- `props`: Pass data to component
```javascript
props: ['propName']
// or
props: {
  propName: {
    type: String,
    required: true,
    default: 'value'
  }
}
```
- `data`: Reactive data `data() { return { key: value } }`
- `computed`: Computed properties
```javascript
computed: {
  fullName() {
    return this.firstName + ' ' + this.lastName
  }
}
```
- `methods`: Component methods
```javascript
methods: {
  myMethod() {
    // logic
  }
}
```
- `watch`: Watch property changes
```javascript
watch: {
  value(newVal, oldVal) {
    // handle change
  }
}
```

## Lifecycle Hooks
- `beforeCreate`
- `created`
- `beforeMount`
- `mounted`
- `beforeUpdate`
- `updated`
- `beforeDestroy`
- `destroyed`

## Event Handling
- Basic event: `@click="handler"`
- Event modifiers:
  - `.stop`: Stop propagation
  - `.prevent`: Prevent default
  - `.capture`: Capture mode
  - `.self`: Trigger if target is element
  - `.once`: Trigger once
  - `.passive`: Improve scrolling performance
- Key modifiers: `@keyup.enter="handler"`

## Slots
- Default slot: `<slot></slot>`
- Named slot: `<slot name="slotName"></slot>`
- Scoped slot:
```vue
<template v-slot:slotName="slotProps">
  {{ slotProps.data }}
</template>
```

## Vue Router
- Install: `vue add router`
- Basic usage:
```javascript
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const routes = [
  { path: '/path', component: ComponentName }
]

const router = new VueRouter({
  routes
})
```
- Navigation: `this.$router.push('/path')`
- Route params: `this.$route.params.id`
- Router link: `<router-link to="/path">Link</router-link>`

## Vuex (State Management)
- Install: `vue add vuex`
- Basic store:
```javascript
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
  state: { count: 0 },
  mutations: {
    increment(state) {
      state.count++
    }
  },
  actions: {
    increment({ commit }) {
      commit('increment')
    }
  },
  getters: {
    count: state => state.count
  }
})
```
- Access: `this.$store.state.count`
- Commit mutation: `this.$store.commit('increment')`
- Dispatch action: `this.$store.dispatch('increment')`

## Vue 3 Composition API
- Setup:
```javascript
import { ref, computed } from 'vue'
export default {
  setup() {
    const count = ref(0)
    const doubled = computed(() => count.value * 2)
    return { count, doubled }
  }
}
```
- Reactive: `const state = reactive({ key: value })`
- Ref: `const value = ref(initialValue)`
- Computed: `const value = computed(() => expression)`
- Watch: `watch(source, callback)`
- Lifecycle hooks:
  - `onMounted(() => {})`
  - `onUnmounted(() => {})`
  - `onBeforeMount(() => {})`
  - `onBeforeUnmount(() => {})`

## Vue 3 Specific
- `defineProps`: Define component props
- `defineEmits`: Define component emits
- `defineExpose`: Expose public methods
- `Teleport`: Render content elsewhere `<Teleport to="body">`
- `Suspense`: Handle async components `<Suspense>`

## Testing
- Install Vue Test Utils: `npm install @vue/test-utils`
- Unit testing: `npm install jest`
- E2E testing: `npm install cypress`

## Common Plugins
- Vue Router: `npm install vue-router`
- Vuex: `npm install vuex`
- Axios: `npm install axios`
- Vuetify: `npm install vuetify`
______________________

> By CISO oswaldo.diaz 
