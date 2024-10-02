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

    static get observedAttributes() {
        return ['text', 'state'];
    }

    attributeChangedCallback(name, oldValue, newValue) {
        if (name === 'text') {
            console.log('attributeChangedCallback - "text" newValue');
            this.updateText(newValue);
        }
        if (name === 'state') {
            console.log('attributeChangedCallback - "state" newValue');
            this.toggleState(newValue);
        }
    }

    connectedCallback() {
        this.shadowRoot.querySelector('#text').style.transition = '0.5s cubic-bezier(1, 0, 0, 1)';

        if (this.hasAttribute('text')) {
            console.log('connectedCallback - Attribute "text" changed.');
            this.updateText(this.getAttribute('text'));
        }
        if (this.hasAttribute('state')) {
            console.log('connectedCallback - Attribute "state" changed.');
            this.toggleState(this.getAttribute('textState'));
        }
    }

    toggleState(newState) {
        const textElement = this.shadowRoot.querySelector('#text');
        textElement.classList.toggle(newState);
        console.log('Toggled class:', newState);
    }

    updateText(newText) {
        this.shadowRoot.querySelector('#text').style.transition = '0.5s cubic-bezier(1, 0, 0, 1)';
        this.shadowRoot.querySelector('#text').innerText = newText;
    }
}

// Define the custom element
customElements.define('my-component', MyComponent);
