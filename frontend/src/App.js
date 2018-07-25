import React, { Component } from 'react'
import ListDeltas from './ListDeltas'
import * as PromptAPI from './PromptAPI'
import CreateSentence from './CreateSentence'
import { Route } from 'react-router-dom'

class App extends Component {
  state = {
    sentenceDeltas: [],
  }
  componentDidMount() {
    PromptAPI.getAll()
      .then((sentenceDeltas) => {
        console.log("PromptAPI.getALl: ", sentenceDeltas);
        this.setState(() => ({
          sentenceDeltas
        }))
      })
  }
  createSentence = (sentence) => {
    console.log("createSentence: ", sentence);
    PromptAPI.create(sentence).then()
  }
  render() {
    return (
      <div>
        <Route exact path='/' render={() => (
          <ListDeltas
            sentenceDeltas={this.state.sentenceDeltas}
          />
          )} />
        <Route path='/create' render={({ history }) => (
          <CreateSentence
              onCreateSentence={(sentence) => {
                this.createSentence(sentence)
                history.push('/')
              }}
              />
          )}
          />

      </div>
    )
  }
}

export default App;
