import React, { Component } from 'react'
import axios from 'axios'

const api_url = process.env.REACT_APP_API_URL

class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {value: ""}

        this.handleSearch = this.handleSearch.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleSearch(event)  {
        this.setState({value: event.target.value})
    }

    async handleSubmit(event) {
        event.preventDefault()
        const response = await axios.get(`${api_url}/name/${this.titleCase(this.state.value)}`)
        const data = response.data
        this.props.restaurantName(data)
    }

    titleCase(str) {
        str = str.toLowerCase().split(' ')
        for(let i = 0; i < str.length; i++) {
            str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1)
        }
        return str.join(' ')
    }

    render() {
        return(
            <div>
            <form onSubmit={this.handleSubmit}>
                <label>Search by Name</label>
                <input type="text" value={this.state.value} onChange={this.handleSearch} />
                <button type="submit">Search</button>
            </form>

            </div>
        )
    }
}

export default Search