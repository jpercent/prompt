import React, {Component} from 'react'
import PropTypes from 'prop-types'
import {Link} from 'react-router-dom'

class ListDeltas extends Component {
 static propTypes = {
     sentenceDeltas: PropTypes.array.isRequired,
   }
  render () {
    console.log(`Props = ${this.props}`, this.props);
    const { sentenceDeltas } = this.props
    let i = 0;
    console.log(sentenceDeltas);
    return (
      <div className='list-deltas'>
        <div className='list-deltas-top'>

        <Link
          to='/create'
          className='add-sentence'
        >Add sentence</Link>
      </div>

        {
          sentenceDeltas.map((delta) => (delta.map((d)=>(
            <p key={i++}>{d}</p>
          ))))
        }
      </div>
    )
  }
}

export default ListDeltas
/*
          <ol className="deltas-list" >
<li key={i++}>
  <div className='delta'>
    <p>{delta}</p>
  </div>
</li>
      </ol>
*/
