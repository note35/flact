class Index extends React.Component {
  render() {
    return (
      <div>
        <Navigator
          title="Example"
        />
        <Content
          name="whatever"
        />
        <Footer
          year="2018"
          team="Kir Chou"
        />
      </div>
    )
  }
}

ReactDOM.render(
  <Index />,
  document.getElementById('index')
)
