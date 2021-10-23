def serialize_minio_object(obj):
    return {
        'object_name': obj.object_name,
        'metadata': obj.metadata,
        'last_modified': obj.last_modified,
        'size': obj.size,
        'content_type': obj.content_type,
        'version_id': obj.version_id
    }

def serialize_minio_list(objects):
    result = []
    for ob in objects:
        result.append(serialize_minio_object(ob))
    return result