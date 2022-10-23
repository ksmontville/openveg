import React, { Component } from 'react'

class ListItem extends Component {

    render() {
        const {restaurantData} = this.props
        return(
            <li key={restaurantData.id}>
                <ul>
                    <li>
                        {restaurantData.name}
                    </li>
                    <li>
                        {restaurantData.description}
                    </li>
                    <li>
                        <a href={restaurantData.web.toString()} target="_blank" rel="noreferrer">{restaurantData.web}</a>
                    </li>
                    <li>
                        Vegan: {restaurantData.vegan.toString()}
                    </li>
                    <li>
                        {restaurantData.address}
                    </li>
                    <li>
                        {restaurantData.city}, {restaurantData.state} {restaurantData.zip}
                    </li>
                </ul>
            </li>
        )
    }
}

export default ListItem