class Footer extends React.Component {
  render() {
    return (
      <footer>
        <div className="footer-copyright center grey lighten-2">
          © {this.props.year} {this.props.team}
        </div>
      </footer>
    )
  }
}
