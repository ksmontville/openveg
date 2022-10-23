import React, { Component } from 'react'
import ListItem from './ListItem'

class List extends Component {
    render() {
        const { data } = this.props
        return(
            <div>
                <ul>
                    {data.map(restaurant => (
                        <ListItem restaurantData={restaurant} /> ))}
                </ul>
            </div>
        )

    }
}

export default List