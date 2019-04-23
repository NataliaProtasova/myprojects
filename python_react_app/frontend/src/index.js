import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

class FetchDemo extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      products: [],
      loading: true,
      error: null
    };
  }

  componentDidMount() {
    axios.get(`http://localhost:8000/api/v1/products/`)
      .then(res => {
		console.log(res);
        // Transform the raw data by extracting the nested products
        const products = res.data.results; //res.data.results.map(obj => obj);
		console.log(products);

        // Update state to trigger a re-render.
        // Clear any errors, and turn off the loading indiciator.
        this.setState({
          products,
          loading: false,
          error: null
        });
      })
      .catch(err => {
        // Something went wrong. Save the error in state and re-render.
        this.setState({
          loading: false,
          error: err
        });
      });
  }

  renderLoading() {
    return <div>Loading...</div>;
  }

  renderError() {
    return (
      <div>
        Uh oh: {this.state.error.message}
      </div>
    );
  }

  renderPosts() {
    if(this.state.error) {
      return this.renderError();
    }

    return (
      <div class="product">
        {this.state.products.map(product =>		  
		  <div>
  		  <h3>{product.name}</h3>
		  <p>{product.description}</p>
		  <img width="500" src={product.photo} />
		  </div>
        )}
      </div>
    );
  }

  render() {
    return (
      <div>
        <h1>{`${this.props.pagetitle}`}</h1>
		<div class="product-list">
        {this.state.loading ?
          this.renderLoading()
          : this.renderPosts()}
		</div>
      </div>
    );
  }
}

ReactDOM.render(
  <FetchDemo pagetitle="Products"/>,
  document.getElementById('root')
);
