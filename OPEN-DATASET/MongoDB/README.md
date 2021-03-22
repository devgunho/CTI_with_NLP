# MongoDB

### dictionary Details

#### LOCATION

- Country

#### THREAT-ACTOR

- MITRE Group ID
- MITRE Group Name

<br/>

### My Own Instructions

#### db.collection.insertMany()

```js
db.collection.insertMany([
  { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
  {
    item: "notebook",
    qty: 50,
    size: { h: 8.5, w: 11, uom: "in" },
    status: "A",
  },
  { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
  {
    item: "planner",
    qty: 75,
    size: { h: 22.85, w: 30, uom: "cm" },
    status: "D",
  },
  {
    item: "postcard",
    qty: 45,
    size: { h: 10, w: 15.25, uom: "cm" },
    status: "A",
  },
]);
```

```js
db.dictionary.update({}, { $rename: { ner: "entity" } }, false, true);
```

```js
db.dictionary.createIndex({ corpus: 1 }, { unique: true });

db.entity.createIndex({ entity: 1 }, { unique: true });
db.entity.insert([{ entity: "IP" }]);
//E11000 duplicate key error collection: CTI-DICTIONARY.entity index: entity_1 dup key: { entity: "IP" }

db.dictionary.getIndexes();
db.dictionary.dropIndexes();
```

#### db.collection.find()

```js
db.getCollection("dictionary").find({ entity: "LOCATION" });

```

#### Add field if conditions are correct

```js
db.dictionary.updateMany(
  { entity: "LOCATION" },
  { $set: { category: "location" } }
);
```

