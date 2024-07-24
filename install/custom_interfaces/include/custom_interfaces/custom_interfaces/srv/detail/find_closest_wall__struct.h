// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:srv/FindClosestWall.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__FIND_CLOSEST_WALL__STRUCT_H_
#define CUSTOM_INTERFACES__SRV__DETAIL__FIND_CLOSEST_WALL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/FindClosestWall in the package custom_interfaces.
typedef struct custom_interfaces__srv__FindClosestWall_Request
{
  uint8_t structure_needs_at_least_one_member;
} custom_interfaces__srv__FindClosestWall_Request;

// Struct for a sequence of custom_interfaces__srv__FindClosestWall_Request.
typedef struct custom_interfaces__srv__FindClosestWall_Request__Sequence
{
  custom_interfaces__srv__FindClosestWall_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__FindClosestWall_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/FindClosestWall in the package custom_interfaces.
typedef struct custom_interfaces__srv__FindClosestWall_Response
{
  bool successful;
} custom_interfaces__srv__FindClosestWall_Response;

// Struct for a sequence of custom_interfaces__srv__FindClosestWall_Response.
typedef struct custom_interfaces__srv__FindClosestWall_Response__Sequence
{
  custom_interfaces__srv__FindClosestWall_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__srv__FindClosestWall_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__FIND_CLOSEST_WALL__STRUCT_H_
