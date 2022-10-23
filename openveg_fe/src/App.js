import React, {Component} from 'react'
import Header from './components/Header'
import Toolbar from './components/toolbar/Toolbar'
import Contribute from './components/Contribute'
import Footer from './components/Footer'


class App extends Component {
    render() {
        return (
            <div className="App">
                <Header />
                <Toolbar />
                <Contribute />
                <Footer />
            </div>
        )
    }
}

export default App