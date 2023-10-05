import {Component} from 'react';

// const displayMessage = ()=> {
//     return 'I need help!';
// }

class Message extends Component{
    render(){
        return <h1>The message says: {this.props.messageCont}</h1>
        // <h1>The Message is: {displayMessage()}</h1>
    }
}

export default Message;