db.zips.aggregate([
    {
        $group: {
            _id: "$city",
            totalZips:{"$count":{ }}
        }
    }
])
