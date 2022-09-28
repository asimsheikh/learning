# AlpineJS 

A summary from the amazing youtube course on https://www.youtube.com/watch?v=5ILDMMLgX0E

## x-bind

This directive is used to change the attribute values on a html element

```HTML
	<button 
	 x-data="{id: ''}"
	 :id="id"
	 @click="id = Math.round(Math.random() * 1000000)"
	 >Button</button>
 ```

The challenge was to iterate through a collection of colors and display divs for
them

```HTML
    <div x-data="{colors: ['red', 'green', 'blue', 'yellow', 'lightblue']}">
        <template x-for="color in colors">
            <div style="width: 40px; height:40px; display: inline-block" :style="{backgroundColor: color}"></div>
        </template>
    </div>
```

```HTML
    <!-- Create a button and 3 inputs
        
        - first input should become text of button
        - second input should become color of button 
        - third input should become button id 
    
    -->

    <div x-data="{text: '', color: '', id: ''}">
        <button x-text="text" :style="{backgroundColor: color}" :id="id"></button>
        <br>
        <input type="text" x-model="text" name="buttonText" placeholder="enter button name">
        <input type="text" x-model="color" name="colorText" placeholder="enter color name">
        <input type="text" x-model="id" name="idText" placeholder="enter id">
    </div>
```
