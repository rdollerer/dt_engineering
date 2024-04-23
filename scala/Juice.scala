class Juice(
    private val name_ : String,
    private val volume_ : Short
  ) extends Product(name_, "Juice") {

  def ==(juice : Juice) : Boolean = this.name_ == juice.name_ && this.volume_ == juice.volume_

  def !=(juice : Juice) : Boolean = !this.==(juice)

  override def toString = s"Juice: ${this.name_} (${this.volume_})"
}