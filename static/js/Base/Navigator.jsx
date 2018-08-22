class Navigator extends React.Component {
  render() {
    return (
      <nav>
        <div class="nav-wrapper black lighten-3">
          <a href="#" class="brand-logo center">
            <i class="material-icons">airline_seat_flat</i>{this.props.title}
          </a>
        </div>
      </nav>
    )
  }
}
