class Fruit(
    private val name_ : String
  ) extends Product(name_, "Fruit") {

  def ==(fruit : Fruit) : Boolean = this.name_ == fruit.name_

  def !=(fruit : Fruit) : Boolean = !this.==(fruit)
}