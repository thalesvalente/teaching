import {
  Controller,
  Get,
  Post,
  Body,
  Param,
  Put,
  Delete,
  UseGuards,
  Req,
} from '@nestjs/common';
import { ScriptService } from './script.service';
import { Role, Script } from '@prisma/client';
import { ApiTags, ApiOperation, ApiResponse, ApiParam } from '@nestjs/swagger';
import { JwtAuthGuard } from 'src/auth/local-auth.guard';
import { CreateScriptDto } from './create-script.dto';
import { Roles } from 'src/auth/roles.decorator';
import { UpdateScriptDto } from './update-script.dto';

@ApiTags('scripts')
@Controller('scripts')
export class ScriptController {
  logger: any;
  constructor(private readonly scriptService: ScriptService) {}

  @UseGuards(JwtAuthGuard)
  @Roles(Role.ADMIN)
  @Get()
  async findAll() {
    return this.scriptService.findAll();
  }

  @UseGuards(JwtAuthGuard)
  @Roles(Role.USER, Role.ADMIN, Role.EMPLOYEE)
  @Post('submit')
  async submitScript(@Req() req, @Body() createScriptDto: CreateScriptDto) {
    const userId = req.user.userId;
    const script = await this.scriptService.createScript(
      userId,
      createScriptDto,
    );
    return script;
  }

  @Get(':id')
  @ApiOperation({ summary: 'Get script by ID' })
  @ApiResponse({ status: 200, description: 'Return script data.' })
  @ApiParam({ name: 'id', required: true, description: 'Script ID' })
  async getScript(@Param('id') id: string): Promise<Script | null> {
    return this.scriptService.findScriptById(Number(id));
  }

  @UseGuards(JwtAuthGuard)
  @Roles(Role.ADMIN)
  @Put(':id')
  async updateScript(
    @Param('id') id: string,
    @Body() updateScriptDto: UpdateScriptDto,
  ) {
    return this.scriptService.updateScript(id, updateScriptDto);
  }

  @UseGuards(JwtAuthGuard)
  @Roles(Role.ADMIN)
  @Delete(':id')
  @ApiOperation({ summary: 'Delete script by ID' })
  @ApiResponse({
    status: 200,
    description: 'The script has been successfully deleted.',
  })
  @ApiParam({ name: 'id', required: true, description: 'Script ID' })
  async deleteScript(@Param('id') id: string) {
    return this.scriptService.deleteScript(id);
  }
}
