# jQuery 

## Selectors
- `$("element")` - Select elements by tag name
- `$("#id")` - Select element by ID
- `$(".class")` - Select elements by class
- `$("[attribute]")` - Select elements with attribute
- `$("parent > child")` - Direct child selector
- `$("ancestor descendant")` - Descendant selector
- `$(":first")` - First matched element
- `$(":last")` - Last matched element
- `$(":even")` - Even-indexed elements
- `$(":odd")` - Odd-indexed elements
- `$(":contains(text)")` - Elements containing text
- `$(":hidden")` - Hidden elements
- `$(":visible")` - Visible elements

## DOM Manipulation
- `.html()` - Get/set HTML content
- `.text()` - Get/set text content
- `.val()` - Get/set form element value
- `.attr()` - Get/set attribute value
- `.removeAttr()` - Remove attribute
- `.addClass()` - Add class
- `.removeClass()` - Remove class
- `.toggleClass()` - Toggle class
- `.append()` - Add content to end
- `.prepend()` - Add content to beginning
- `.after()` - Insert content after
- `.before()` - Insert content before
- `.remove()` - Remove elements
- `.empty()` - Remove all child nodes

## Events
- `.on(event, handler)` - Attach event handler
- `.off(event)` - Remove event handler
- `.click()` - Bind/trigger click event
- `.dblclick()` - Bind/trigger double click
- `.hover()` - Bind hover events
- `.mouseover()` - Bind mouseover event
- `.mouseout()` - Bind mouseout event
- `.focus()` - Bind/trigger focus event
- `.blur()` - Bind/trigger blur event
- `.change()` - Bind/trigger change event
- `.submit()` - Bind/trigger form submit
- `.keydown()` - Bind keydown event
- `.keyup()` - Bind keyup event

## Effects & Animations
- `.show()` - Display element
- `.hide()` - Hide element
- `.toggle()` - Toggle show/hide
- `.fadeIn()` - Fade in element
- `.fadeOut()` - Fade out element
- `.fadeTo()` - Fade to opacity
- `.slideDown()` - Slide down element
- `.slideUp()` - Slide up element
- `.slideToggle()` - Toggle slide
- `.animate()` - Custom animations
- `.stop()` - Stop animations
- `.delay()` - Delay animations

## AJAX
- `$.ajax()` - Perform AJAX request
- `.get()` - GET request
- `.post()` - POST request
- `$.getJSON()` - GET JSON data
- `.load()` - Load data into element
- `$.ajaxSetup()` - Set default AJAX settings

## DOM Traversal
- `.find()` - Find descendants
- `.parent()` - Get parent element
- `.parents()` - Get all ancestors
- `.closest()` - Get closest ancestor
- `.children()` - Get direct children
- `.siblings()` - Get siblings
- `.next()` - Get next sibling
- `.prev()` - Get previous sibling
- `.first()` - Get first element
- `.last()` - Get last element
- `.filter()` - Filter matched set
- `.not()` - Remove elements from set

## Utilities
- `$.each()` - Iterate over array/objects
- `$.extend()` - Merge objects
- `$.grep()` - Filter array
- `$.map()` - Transform array
- `$.trim()` - Trim string
- `$.inArray()` - Check if value exists in array
- `$.isArray()` - Check if is array
- `$.isFunction()` - Check if is function
- `$.parseJSON()` - Parse JSON string
- `$.type()` - Determine data type

## Chaining
- Most jQuery methods return the jQuery object, allowing method chaining:
```javascript
$("selector").css().addClass().animate()
```

## Notes
- Use `$(document).ready()` or `$(function() {})` to ensure DOM is loaded
- jQuery methods typically accept optional parameters for customization
- Use `event.preventDefault()` to prevent default browser behavior
- Check jQuery version compatibility for specific methods
- Use `.on()` instead of older `.bind()`, `.live()`, or `.delegate()`

____________________

> By CISO oswaldo.diaz
