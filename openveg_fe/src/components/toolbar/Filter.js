import React, { Component } from 'react'
import axios from "axios";

const api_url = process.env.REACT_APP_API_URL

class Filter extends Component {
    constructor(props) {
        super(props);
        this.state = {vegan: false, selectedState: ""}

        this.handleChange = this.handleChange.bind(this)
        this.handleData = this.handleData.bind(this)
    }

    handleChange = async () => {
        this.setState({vegan: !this.state.vegan, selectedState: this.props.currentState}, await this.handleData)
    }

    handleData = async () => {
        this.props.vegan(this.state.vegan)
        const response = await axios.get(`${api_url}/?state=${this.state.selectedState.toLowerCase()}&vegan=${this.state.vegan}`)
        const data = response.data
        this.props.veganData(data)
    }

    render() {
        return (
            <div>
                <label>Show Only Vegan Restaurants</label>
                <input name="vegan" type="checkbox" value={this.state.vegan}
                       checked={this.state.vegan} onChange={this.handleChange}/>
            </div>
        )
    }
}

export default Filter