class VendingMachine(
    private val capacity_ : Int
  ) {

  private var products_ : List[Product] = List[Product]()
  private var quantity_ = 0

  def add_update_quantity_(product : Product) : Boolean = {
    product match {
      case p : Juice => {
        if (this.capacity_ - this.quantity_ > 2) {
          this.quantity_ += 2
          return true
        }
        return false
      }
      case p : Fruit => {
        if (this.capacity_ - this.quantity_ > 1) {
          this.quantity_ += 1
          return true
        }
        return false
      }
    }
  }

  def add(product : Product) : Unit = {
    if (add_update_quantity_(product)) {
      println(s"Adding ${product}")
      this.products_ = this.products_ :+ product
    }
    else
      println(s"Not enough space for ${product}")
  }

  def remove_update_quantity_(product : Product) : Unit = {
    product match {
      case p : Juice => {
        this.quantity_ -= 2
      }
      case p : Fruit => {
        this.quantity_ -= 1
      }
    }
  }

  def remove(product : Product) : Unit = {
    val products_length = this.products_.length
    this.products_ = this.products_.filter(_ != product)
    if (products_length != this.products_.length) {
      remove_update_quantity_(product)
      println(s"${product} deleted")
    }
    else
      println(s"${product} not found")
  }

  override def toString : String = {
    if (this.quantity_ > 0) {
      s"Vending machine has ${this.capacity_ - this.quantity_} space left\nIt contains: " + this.products_.map(_.name).mkString("; ")
    }
    else
      "Vending machine is empty"
  }
}