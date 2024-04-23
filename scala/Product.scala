abstract class Product(
    private val name_ : String,
    private val type_ : String
  ) {

  def name = this.name_

  override def toString = s"${this.type_}: ${this.name_}"
}