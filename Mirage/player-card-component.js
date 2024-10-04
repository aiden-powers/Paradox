class PlayerCardComponent extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: 'open' });

        shadowRoot.innerHTML = `
            <link rel="stylesheet" href="player-card.css">
            <style>
                .move100 {
                    width: 256px;
                    height: 128px;
                }
            </style>
            <div class="player_card_base" id="playerCard">
                <p class="player_card_text_character" id="character"> Character </p>
            <p class="player_card_text_username" id="username"> Username </p>
            </div>
        `;
    }

    static attributesMap = {
        state: 'updateState',
        //text: 'updateText',
        character: 'character',
        username: 'username',
        transition: 'updateTransition',
    };

    static get observedAttributes() {return Object.keys(PlayerCardComponent.attributesMap);}
    attributeChangedCallback(name, oldValue, newValue) {const method = PlayerCardComponent.attributesMap[name];if (method && typeof this[method] === 'function') {this[method](newValue);}}
    connectedCallback() {Object.keys(PlayerCardComponent.attributesMap).forEach((attr) => {if (this.hasAttribute(attr)) {const method = PlayerCardComponent.attributesMap[attr];this[method](this.getAttribute(attr));}})}

    updateState(newState) {
        console.log('updateState');
        // Handle state change
        const element = this.shadowRoot.querySelector('#playerCard');
        const stateIndicator = newState.slice(-2); // _1 true, _0 false
        const stateName = newState.slice(0, -2); // name excluding indicator
        if (stateIndicator === '_1') {if (!element.classList.contains(stateName)) {element.classList.add(stateName);}} // stateName does not already exist, execute addition
        if (stateIndicator === '_0') {if (element.classList.contains(stateName)) {element.classList.remove(stateName);}} // stateName exists, execute removal
    }

    updateTransition(newTransition) {
        console.log('Update Transition')
        this.shadowRoot.querySelector('#playerCard').style.transition = newTransition;
    }

    updateText(newText) {
        // Handle text change
        console.log('Update Text')
        //this.shadowRoot.querySelector('#text').innerText = newText;
    }
}

// Define the custom element
customElements.define('player-card', PlayerCardComponent);