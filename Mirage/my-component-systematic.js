class MyComponent extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: 'open' });

        shadowRoot.innerHTML = `
            <style>
                .component {
                    color: blue;
                    border: 1px solid black;
                    padding: 10px;
                    margin: 10px;
                }
                .move100 {
                    transform: translateX(100px);
                }
            </style>
            <div class="component">
                <p id="text">Default Text</p>
            </div>
        `;
    }

    static attributesMap = {
        state: 'updateState',
        text: 'updateText',
        transition: 'updateTransition',
    };

    static get observedAttributes() {return Object.keys(MyComponent.attributesMap);}
    attributeChangedCallback(name, oldValue, newValue) {const method = MyComponent.attributesMap[name];if (method && typeof this[method] === 'function') {this[method](newValue);}}
    connectedCallback() {Object.keys(MyComponent.attributesMap).forEach((attr) => {if (this.hasAttribute(attr)) {const method = MyComponent.attributesMap[attr];this[method](this.getAttribute(attr));}})}

    updateState(newState) {
        console.log('updateState');
        // Handle state change
        const element = this.shadowRoot.querySelector('#text');
        const stateIndicator = newState.slice(-2); // _1 true, _0 false
        const stateName = newState.slice(0, -2); // name excluding indicator
        if (stateIndicator === '_1') {if (!element.classList.contains(stateName)) {element.classList.add(stateName);}} // stateName does not already exist, execute addition
        if (stateIndicator === '_0') {if (element.classList.contains(stateName)) {element.classList.remove(stateName);}} // stateName exists, execute removal
    }

    updateTransition(newTransition) {
        console.log('Update Transition')
        this.shadowRoot.querySelector('#text').style.transition = '0.5s cubic-bezier(1, 0, 0, 1)';
    }

    updateText(newText) {
        // Handle text change
        console.log('Update Text')
        this.shadowRoot.querySelector('#text').innerText = newText;
    }
}

// Define the custom element
customElements.define('my-component', MyComponent);