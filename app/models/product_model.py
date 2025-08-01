from . import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum, Table, relationship, datetime, enum, Base, TIMESTAMP, text

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("UserModel")