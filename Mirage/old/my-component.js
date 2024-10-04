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

    static stateAttribute = 'state';
    static textAttribute = 'text';

    static get observedAttributes() {
        // Declare naming
        return [MyComponent.textAttribute, MyComponent.stateAttribute];
    }

    attributeChangedCallback(name, oldValue, newValue) {
        // Declare callback functions
        if (name === MyComponent.textAttribute) {this.updateText(newValue);}
        if (name === MyComponent.stateAttribute) {this.setState(newValue);}
    }

    connectedCallback() {
        this.shadowRoot.querySelector('#text').style.transition = '0.5s cubic-bezier(1, 0, 0, 1)'; // FIXME: not here

        if (this.hasAttribute(MyComponent.textAttribute)) {this.updateText(this.getAttribute(MyComponent.textAttribute));}
        if (this.hasAttribute(MyComponent.stateAttribute)) {this.setState(this.getAttribute(MyComponent.stateAttribute));}
    }

    setState(newState) {
        const element = this.shadowRoot.querySelector('#text'); // FIXME: element selection should be handled by the attribute route logic? state_boolean for an update is not good enough. maybe id_state_boolean?
        const stateIndicator = newState.slice(-2); // _1 true, _0 false
        const stateName = newState.slice(0, -2); // name excluding indicator
        if (stateIndicator === '_1') {if (!element.classList.contains(stateName)) {element.classList.add(stateName);}} // stateName does not already exist, execute addition
        if (stateIndicator === '_0') {if (element.classList.contains(stateName)) {element.classList.remove(stateName);}} // stateName exists, execute removal
    }

    updateText(newText) {
        this.shadowRoot.querySelector('#text').innerText = newText;
    }
}

// Define the custom element
customElements.define('my-component', MyComponent);