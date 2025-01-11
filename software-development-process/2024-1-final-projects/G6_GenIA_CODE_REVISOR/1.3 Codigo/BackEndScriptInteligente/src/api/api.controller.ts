import {
  Controller,
  Post,
  Get,
  Delete,
  Param,
  Body,
  UseGuards,
} from '@nestjs/common';
import { ApiService } from './api.service';
import { CreateApiDto } from './create-api.dto';
import { JwtAuthGuard } from '../auth/local-auth.guard';
import { Roles } from '../auth/roles.decorator';
import { Role } from '@prisma/client';

@Controller('apis')
export class ApiController {
  constructor(private readonly apiService: ApiService) {}

  @UseGuards(JwtAuthGuard)
  @Roles(Role.ADMIN)
  @Post()
  async createApi(@Body() createApiDto: CreateApiDto) {
    return this.apiService.createApi(createApiDto);
  }

  @UseGuards(JwtAuthGuard)
  @Roles(Role.ADMIN)
  @Get()
  async findAllApis() {
    return this.apiService.findAllApis();
  }

  @UseGuards(JwtAuthGuard)
  @Roles(Role.ADMIN)
  @Delete(':id')
  async deleteApi(@Param('id') id: string) {
    return this.apiService.deleteApi(Number(id));
  }
}
