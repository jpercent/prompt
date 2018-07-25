import React, { Component } from 'react'
import {Link} from 'react-router-dom'
import serializeForm from 'form-serialize'

class CreateSentence extends Component {
  handleSubmit = (e) => {
    e.preventDefault();
    const values = serializeForm(e.target, { hash: true});
    console.log('values', values);

    if (this.props.onCreateSentence) {
      this.props.onCreateSentence(values);
    }
  }
  render () {
    return (
      <div>
        <Link className="close-create-sentence" to='/'>
          Close
        </Link>
        <form onSubmit={this.handleSubmit} className='create-sentence-form'>
          <div className='create-sentence-details'>
            <input type='text' name='question' placeholder='Question'/>
            <button>Add sentence</button>
          </div>
        </form>
    </div>
    );
  }
}

export default CreateSentence
